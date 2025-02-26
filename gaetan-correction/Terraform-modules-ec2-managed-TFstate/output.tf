# Output the public IP address of the EC2 instance
output "instance_public_ip" {
  value       = module.ec2_instance.instance_public_ip
  description = "The public IP address of the EC2 instance"
}