variable "region" {
  type = string
}

variable "instance_type" {
  type = string
}
variable "key_name" {
  type = string
  default = "key_terraform"
}

variable "availability_zones" {
  type = list(string)
}

variable "amis" {
  type = map(any)
  default = {
    "us-east-2" : "ami-05fb0b8c1424f266b"
    "us-west-2" : "ami-008fe2fc65df48dac"
  }
}
