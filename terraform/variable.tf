variable "s3_bucket"{
    description = "Bucket name for s3"
    type  = string
    default = "anand-reddit-bucket"

}
variable "db_password"{
    description = "Redshift password for master DB"
    type  = string
    default = "Anand2003"

}
variable "aws_region" {
  description = "Region for AWS"
  type        = string
  default     = "ap-south-1"
}

