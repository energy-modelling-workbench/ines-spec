# Changelog
All structural changes to ines-spec are documented here. Changes to the example data set are not documented. Changes/additions to parameter descriptions are not documented unless there is a change in the unit of measure.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)

## [Unreleased]

## [0.3.0]

### Added 

- unit_flow__unit_flow class with parameters to set constraints between the two nodes
- unit__to_node and node__to_unit are now based on superclass unit_flow

### Changed

- Fixed typos in parameter descriptions (MWh to MW in couple of instances)

## [0.2.0]

### Added 

- node entity_class has a new parameter co2_content
- unit__to_node and node__to_unit classes have a new parameter nox_emission_rate

## [0.1.0]

### Added

- The initial data structure for ines-spec. Sufficient feature set for planning problems using energy transfers and simple energy conversions.
