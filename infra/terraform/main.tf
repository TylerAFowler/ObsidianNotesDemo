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
resource "oci_objectstorage_object_lifecycle_policy" "clips" {
  namespace = var.namespace
  bucket    = oci_objectstorage_bucket.clips.name
  rules {
    name        = "archive-after-90-days"
    action      = "ARCHIVE"
    time_amount = 90
    time_unit   = "DAYS"
    is_enabled  = true
  }
}
