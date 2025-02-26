# Configure the S3 backend for Terraform state
# Terraform Block

terraform {
  backend "s3" {
    bucket         = "assignment9-bucket-102824"
    key            = "terraform.tfstate"
    region         = "us-east-1" # Change this to match your S3 bucket's region
    encrypt        = true
    dynamodb_table = "db-table"
  }
}