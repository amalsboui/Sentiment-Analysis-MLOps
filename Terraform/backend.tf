terraform {
  cloud {
    organization = "hophopp_cc"

    workspaces {
      name = "sentiment-azure-storage"
    }
  }
}