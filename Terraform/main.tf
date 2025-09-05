# Random suffix to make storage name unique
resource "random_integer" "suffix" {
  min = 1000
  max = 9999
}

# Resource group
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

# Storage account
resource "azurerm_storage_account" "storage" {
  name                     = "sentimentmodels${random_integer.suffix.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# Blob container
resource "azurerm_storage_container" "models" {
  name                  = var.storage_container_name
  storage_account_id    = azurerm_storage_account.storage.id
  container_access_type = "private"
}


# Output storage account and container info
output "storage_account_name" {
  value = azurerm_storage_account.storage.name
}

output "storage_container_name" {
  value = azurerm_storage_container.models.name
}
