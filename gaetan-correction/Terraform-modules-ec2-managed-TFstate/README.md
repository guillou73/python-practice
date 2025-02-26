Terraform Infrastructure as Code (IaC)
Objective:
The goal of this assignment is to give hands-on experience with Infrastructure as Code (IaC)
using Terraform to manage and provision resources on AWS, focusing on best practices, remote
state management, and cost-efficiency.
Part 1: Terraform Basics and State Management
1. Define AWS Provider:
○ Use the AWS provider to define the connection to your AWS account.
○ Set up environment variables for AWS credentials or use AWS CLI
authentication.
2. Provision Basic AWS Infrastructure:
○ Write Terraform code to provision an EC2 instance.
■ Choose a cost-effective instance type (e.g., t2.micro or t3.micro)
that qualifies for AWS Free Tier if available.
○ Define an S3 bucket for remote state storage.
○ Create a DynamoDB table for state file locking.
Part 2: Terraform State Management and Remote Backend
5. Remote Backend Setup:
○ Configure Terraform to use the S3 bucket as a remote backend to store your
state file.
○ Enable state locking using the DynamoDB table to prevent simultaneous
modifications.
○ Update your main.tf to include the remote backend block.
6. Workspaces:
○ Use Terraform workspaces to manage different environments (e.g., dev, staging,
prod).
○ Create at least two workspaces (dev and prod).
Part 3: Modules and Reusable Code
7. Create Reusable Modules:
○ Refactor your Terraform code into a reusable module for the EC2 instance.
○ Ensure that this module can be reused in both dev and prod workspaces with
different configurations (e.g., tags or instance size).
Part 4: Version Control and Remote Backend
8. Version Control:
○ Initialize a Git repository for your Terraform project.
○ Push your code to a remote Git repository (e.g., GitHub).
○ Use .gitignore to ignore sensitive data such as Terraform state files and
variables.
Part 5: Testing and Validation
9. Validation and Linting:
○ Use terraform validate to ensure your configuration files are syntactically
correct.
○ Use a Terraform linting tool (e.g., tflint) to catch common configuration errors.
Part 6: Clean Up and Cost Management
10. Cost Efficiency and Cleanup:
○ Before submission, make sure to destroy the resources to avoid unnecessary
charges.
○ Use terraform destroy to delete the EC2 instance, S3 bucket, and
DynamoDB table.
○ Ensure you understand the costs of the resources you provision and explore
Free Tier options where available.
Deliverables:
1. Terraform Configuration Files:
○ Submit your Terraform configuration files (main.tf, variables.tf,
outputs.tf, etc.).
2. Module:
○ Submit the module you created for EC2 provisioning.
3. Workspace Usage:
○ Document the steps you took to create workspaces and provision resources in
multiple environments.
4. Testing and Validation:
○ Submit the output of terraform validate and linting.
5. Git Repository:
○ Provide a link to your Git public repository with the complete code.
Additional Considerations:
● Be mindful of AWS costs. Provision resources only for the duration of this assignment,
and ensure they are terminated afterward.
● Use Free Tier eligible services where applicable to minimize costs.
● Pay attention to modular design and environment separation using workspaces to
simulate real-world scenarios.

NOTES:
To Create an ec2 in the dev environment, switch to the dev workspace with the commands: 
1- terraform workspace new "dev"
2- terraform init
3- terraform apply -var-file="dev.tfvars"

repeat the same steps to create a new instance in a separate workspace, granted the ${workspace}.tfvars file exist in the project root directory

##Happy Learning##
