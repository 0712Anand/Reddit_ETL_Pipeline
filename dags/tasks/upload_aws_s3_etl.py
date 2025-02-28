import boto3
import botocore
import configparser
import pathlib
import sys
from validate.validation import validate_input

"""
Part of DAG. Take Reddit data and upload to S3 bucket. Takes one command line argument of format YYYYMMDD. 
This represents the file downloaded from Reddit, which will be in the /tmp folder.
"""

# Load AWS credentials
parser = configparser.ConfigParser()
script_path = pathlib.Path(__file__).parent.resolve()
parser.read(f"{script_path}/configuration.conf")
BUCKET_NAME = parser.get("aws_config", "bucket_name")
AWS_REGION = parser.get("aws_config", "aws_region")
AWS_PROFILE = parser.get("aws_config", "aws_profile", fallback="default")  # Use the profile name for SSO

# TODO Improve error handling
try:
    output_name = sys.argv[1]
except Exception as e:
    print(f"Command line argument not passed. Error {e}")
    sys.exit(1)

# Name for our S3 file
FILENAME = f"{output_name}.csv"
KEY = FILENAME


def main():
    """Upload input file to S3 bucket"""
    validate_input(output_name)
    conn = connect_to_s3()
    create_bucket_if_not_exists(conn)
    upload_file_to_s3(conn)


def connect_to_s3():
    """Connect to S3 Instance using AWS SSO"""
    try:
        # Create a boto3 session using the configured AWS profile (which should be set up for SSO)
        session = boto3.Session(profile_name=AWS_PROFILE)
        conn = session.resource("s3")  # Use session to get the S3 resource
        return conn
    except Exception as e:
        print(f"Can't connect to S3. Error: {e}")
        sys.exit(1)


def create_bucket_if_not_exists(conn):
    """Check if bucket exists and create if not"""
    exists = True
    try:
        conn.meta.client.head_bucket(Bucket=BUCKET_NAME)
    except botocore.exceptions.ClientError as e:
        error_code = e.response["Error"]["Code"]
        if error_code == "404":
            exists = False
    if not exists:
        conn.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={"LocationConstraint": AWS_REGION},
        )


def upload_file_to_s3(conn):
    """Upload file to S3 Bucket"""
    conn.meta.client.upload_file(
        Filename="/tmp/" + FILENAME, Bucket=BUCKET_NAME, Key=KEY
    )


if __name__ == "__main__":
    main()
