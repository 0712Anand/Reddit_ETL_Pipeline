variable "s3_bucket"{
    description = "Bucket name for s3"
    type  = string
    default = "xx"

}
variable "db_password"{
    description = "Redshift password for master DB"
    type  = string
    default = "xx"

}
variable "aws_region" {
  description = "Region for AWS"
  type        = string
  default     = "x"
}

