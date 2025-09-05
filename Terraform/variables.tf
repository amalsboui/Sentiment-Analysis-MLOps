variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "sentiment-models-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "North Europe"
}

variable "storage_container_name" {
  description = "Blob container name"
  type        = string
  default     = "models"
}
