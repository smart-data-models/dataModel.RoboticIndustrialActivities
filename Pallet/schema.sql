/* (Beta) Export of data model Pallet of the subject dataModel.RoboticIndustrialActivities for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Pallet_manufacturabilityOnFlexEdge_type AS ENUM ('cannotPickUp', 'canPickUpOnly', 'canProcess');
CREATE TYPE Pallet_status_type AS ENUM ('empty', 'filled', 'loading', 'unloading');
CREATE TYPE Pallet_type AS ENUM ('Pallet');
CREATE TABLE Pallet (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "manufacturabilityOnFlexEdge" Pallet_manufacturabilityOnFlexEdge_type,
  "name" TEXT,
  "owner" JSON,
  "palletId" TEXT,
  "priority" NUMERIC,
  "refGoingTo" JSON,
  "refPalletLocation" JSON,
  "seeAlso" JSON,
  "source" TEXT,
  "status" Pallet_status_type,
  "timeOfLoading" TEXT,
  "type" Pallet_type
);