from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class OperatingMode(Enum):
    T1 = '#T1'
    T2 = '#T2'
    AUT = '#AUT'
    EXT = '#EXT'


class ProState0(Enum):
    P_FREE = '#P_FREE'
    P_ACTIVE = '#P_ACTIVE'
    P_END = '#P_END'
    P_RESET = '#P_RESET'
    P_STOP = '#P_STOP'


class ProState1(Enum):
    P_FREE = '#P_FREE'
    P_ACTIVE = '#P_ACTIVE'
    P_END = '#P_END'
    P_RESET = '#P_RESET'
    P_STOP = '#P_STOP'


class Type6(Enum):
    RobotArm = 'RobotArm'


class RobotArm(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    angleAxis1: Optional[float] = Field(
        None, description='Angle of the first axis on the robot arm'
    )
    angleAxis2: Optional[float] = Field(
        None, description='Angle of the second axis on the robot arm'
    )
    angleAxis3: Optional[float] = Field(
        None, description='Angle of the third axis on the robot arm'
    )
    angleAxis4: Optional[float] = Field(
        None, description='Angle of the fourth axis on the robot arm'
    )
    angleAxis5: Optional[float] = Field(
        None, description='Angle of the fifth axis on the robot arm'
    )
    angleAxis6: Optional[float] = Field(
        None, description='Angle of the sixth axis on the robot arm'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    baseA: Optional[float] = Field(
        None, description='Actual a value for the definition of the base frame'
    )
    baseB: Optional[float] = Field(
        None, description='Actual b value for the definition of the base frame'
    )
    baseC: Optional[float] = Field(
        None, description='Actual c value for the definition of the base frame'
    )
    baseX: Optional[float] = Field(
        None, description='Actual x value for the definition of the base frame'
    )
    baseY: Optional[float] = Field(
        None, description='Actual y value for the definition of the base frame'
    )
    baseZ: Optional[float] = Field(
        None, description='Actual z value for the definition of the base frame'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    drivesOff: Optional[bool] = Field(
        None, description='Status of signal to turn the Robot Drives to off'
    )
    drivesOn: Optional[bool] = Field(None, description='Status of the Robot Drives')
    emergencyStop: Optional[bool] = Field(
        None, description='Readiness of the emergency circuit of the robot'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maxTorqueAxis1: Optional[float] = Field(
        None, description='Maximal torque of the first axis of the robot arm'
    )
    maxTorqueAxis2: Optional[float] = Field(
        None, description='Maximal torque of the second axis of the robot arm'
    )
    maxTorqueAxis3: Optional[float] = Field(
        None, description='Maximal torque of the third axis of the robot arm'
    )
    maxTorqueAxis4: Optional[float] = Field(
        None, description='Maximal torque of the fourth axis of the robot arm'
    )
    maxTorqueAxis5: Optional[float] = Field(
        None, description='Maximal torque of the fifth axis of the robot arm'
    )
    maxTorqueAxis6: Optional[float] = Field(
        None, description='Maximal torque of the sixth axis of the robot arm'
    )
    maxVelocityAxis1: Optional[float] = Field(
        None, description='Maximal Velocity of the first axis of the robot arm'
    )
    maxVelocityAxis2: Optional[float] = Field(
        None, description='Maximal Velocity of the second axis of the robot arm'
    )
    maxVelocityAxis3: Optional[float] = Field(
        None, description='Maximal Velocity of the third axis of the robot arm'
    )
    maxVelocityAxis4: Optional[float] = Field(
        None, description='Maximal Velocity of the fourth axis of the robot arm'
    )
    maxVelocityAxis5: Optional[float] = Field(
        None, description='Maximal Velocity of the fith axis of the robot arm'
    )
    maxVelocityAxis6: Optional[float] = Field(
        None, description='Maximal Velocity of the sixth axis of the robot arm'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operatingMode: Optional[OperatingMode] = Field(
        None,
        description='State of the turn key switch on top of the robot control panel',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    peripheryReady: Optional[bool] = Field(
        None, description='Readiness of all peripheral devices around the robot'
    )
    positionA: Optional[float] = Field(
        None,
        description='Actual a (rotation around z axis) coordinate of the robot position (with the actual tool and base coordinates)',
    )
    positionB: Optional[float] = Field(
        None,
        description='Actual b (rotation around y axis) coordinate of the robot position (with the actual tool and base coordinates)',
    )
    positionC: Optional[float] = Field(
        None,
        description='Actual c (rotation around x axis) coordinate of the robot position (with the actual tool and base coordinates)',
    )
    positionX: Optional[float] = Field(
        None,
        description='Actual x coordinate of the robot position (with the actual tool and base coordinates)',
    )
    positionY: Optional[float] = Field(
        None,
        description='Actual y coordinate of the robot position (with the actual tool and base coordinates)',
    )
    positionZ: Optional[float] = Field(
        None,
        description='Actual z coordinate of the robot position (with the actual tool and base coordinates)',
    )
    proState0: Optional[ProState0] = Field(None, description='Status of the Robot PLC')
    proState1: Optional[ProState1] = Field(
        None, description='Status of the Robot Program Interpreter'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    serialNumber: Optional[float] = Field(
        None, description='The robot identifier, makes it unique in the world'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    toolA: Optional[float] = Field(
        None, description='Actual a value for the definition of the tool frame'
    )
    toolB: Optional[float] = Field(
        None, description='Actual b value for the definition of the tool frame'
    )
    toolC: Optional[float] = Field(
        None, description='Actual c value for the definition of the tool frame'
    )
    toolX: Optional[float] = Field(
        None, description='Actual x value for the definition of the tool frame'
    )
    toolY: Optional[float] = Field(
        None, description='Actual y value for the definition of the tool frame'
    )
    toolZ: Optional[float] = Field(
        None, description='Actual z value for the definition of the tool frame'
    )
    torqueAxis1: Optional[float] = Field(
        None, description='Actual torque of the first axis of the robot arm'
    )
    torqueAxis2: Optional[float] = Field(
        None, description='Actual torque of the second axis of the robot arm'
    )
    torqueAxis3: Optional[float] = Field(
        None, description='Actual torque of the third axis of the robot arm'
    )
    torqueAxis4: Optional[float] = Field(
        None, description='Actual torque of the fourth axis of the robot arm'
    )
    torqueAxis5: Optional[float] = Field(
        None, description='Actual torque of the fifth axis of the robot arm'
    )
    torqueAxis6: Optional[float] = Field(
        None, description='Actual torque of the sixth axis of the robot arm'
    )
    type: Optional[Type6] = Field(
        None, description='It has to be RobotArm. NGSI Entity type'
    )
    velocityAxis1: Optional[float] = Field(
        None, description='Actual Velocity of the first axis of the robot arm'
    )
    velocityAxis2: Optional[float] = Field(
        None, description='Actual Velocity of the second axis of the robot arm'
    )
    velocityAxis3: Optional[float] = Field(
        None, description='Actual Velocity of the third axis of the robot arm'
    )
    velocityAxis4: Optional[float] = Field(
        None, description='Actual Velocity of the fourth axis of the robot arm'
    )
    velocityAxis5: Optional[float] = Field(
        None, description='Actual Velocity of the fifth axis of the robot arm'
    )
    velocityAxis6: Optional[float] = Field(
        None, description='Actual Velocity of the sixth axis of the robot arm'
    )
