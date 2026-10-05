terraform {
  required_providers { oci = { source = "oracle/oci", version = "~> 6.10" } }
}

module "network" {
  source         = "./modules/network"
  compartment_id = var.compartment_id
  cidr_block     = "10.40.0.0/16"
}

resource "oci_objectstorage_bucket" "clips" {
  compartment_id = var.compartment_id
  namespace      = var.namespace
  name           = "roadview-clips"
  versioning     = "Disabled"
}
