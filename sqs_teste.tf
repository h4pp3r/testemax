provider "aws" {
access_key = "${ACCESS_KEY}"
secret_key = "${SECRET_KEY}"
region     = "eu-east-2"
}

resource "aws_sqs_queue" "terraform_queue"{
name = "testetecnico-queue--01"
delay_seconds = 120
max_message_size = 2048
message_retention_seconds = 86400
receive_wait_time_seconds = 10
}
