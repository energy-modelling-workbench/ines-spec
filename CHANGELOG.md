# Changelog
All structural changes to ines-spec are documented here. Changes to the example data set are not documented. Changes/additions to parameter descriptions are not documented unless there is a change in the unit of measure.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)

## [Unreleased]

## [0.4.0]

### Added

- years_represented parameter to the period class
- Maximum and minimum investment limits for aggregated flow and storage capacities using sets (set has new parameters: invest_max_period, invest_max_total, invest_min_period, invest_min_total)
- Maximum and minimum limits for the aggregated flows using sets (set has new parameters: max_cumulative_flow, max_instant_flow, min_cumulative_flow, min_instant_flow)
- New class 'set__unit_flow' to replace 'set__node__unit'
- Added inertia_constant for unit flows and inertia_limit for sets of nodes
- Added is_non_synchronous for unit flows and links as well as non_synchronous_share for sets of nodes

### Removed
- Class 'set__node__unit' (replaced by 'set__unit_flow')

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
