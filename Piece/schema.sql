/* (Beta) Export of data model Piece of the subject dataModel.RoboticIndustrialActivities for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Piece_manufacturabilityOnFlexEdge_type AS ENUM ('canPickUpOnly', 'cannotPickUp', 'canProcess');
CREATE TYPE Piece_status_type AS ENUM ('created', 'inProcess', 'finished');
CREATE TYPE Piece_type AS ENUM ('Piece');
CREATE TABLE Piece (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "manufacturabilityOnFlexEdge" Piece_manufacturabilityOnFlexEdge_type,
  "name" TEXT,
  "owner" JSON,
  "pieceID" TEXT,
  "refPieceLocation" JSON,
  "seeAlso" JSON,
  "sequenceNumber" NUMERIC,
  "source" TEXT,
  "status" Piece_status_type,
  "timeEstimatedOnFlexEdge" NUMERIC,
  "type" Piece_type,
  "weight" NUMERIC
);