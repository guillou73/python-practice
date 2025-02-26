provider "aws" {
  region = var.aws_region
}
# Terraform Block
terraform {

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
module "ec2_instance" {
  source = "./modules/ec2_instance"

  aws_region          = var.aws_region
  ami_id              = var.ami_id
  instance_type       = var.instance_type
  instance_name       = var.instance_name
  dynamodb_table_name = var.dynamodb_table_name
}