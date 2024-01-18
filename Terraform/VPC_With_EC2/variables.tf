variable "region" {
  type = string
  default = "us-west-2"
}

variable "instance_type" {
  type = string
  default = "t3.micro"
}
variable "key_name" {
  type = string
  default = "key_terraform"
}

variable "availability_zones" {
  type = list(string)
   default = ["not-opted-in", "opted-in"]
}

variable "workstation_ip" {
  type = string
  default = "0.0.0.0/0"
}

variable "amis" {
  type = map(any)
  default = {
    "us-east-2" : "ami-08e6b682a466887dd"
    "us-west-2" : "ami-0af6e2b3ada249943"
  }
}
