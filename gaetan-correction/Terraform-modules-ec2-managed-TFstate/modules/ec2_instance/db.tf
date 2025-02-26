# Create a DynamoDB table for state locking
resource "aws_dynamodb_table" "terraform_lock" {
  name           = var.dynamodb_table_name
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
}