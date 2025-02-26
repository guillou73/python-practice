# Output the public IP address of the EC2 instance
output "instance_public_ip" {
  value       = aws_instance.ec2-server.public_ip
  description = "The public IP address of the EC2 instance"
}