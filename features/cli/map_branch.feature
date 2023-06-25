Feature: Map release branch to tyk docs release branch
    In order to synchronise OAS API definitions to tyk-docs,
    As a DX team member
    When the GitHub action runs
    I want to map from source branch release-x.y.z to minor release-x.y

    Scenario Outline: Valid source branch name
        Given the source branch is named <source_branch>
        When the map_branch command is run
        Then the mapped branch name should be <mapped_branch>

            Examples: Branches
                | source_branch  | mapped_branch        |
                | release-5-lts  | release-5            |
                | release-4.2.3  | release-4.2          |

    Scenario Outline: Invalid source branch name
        Given the source branch is named <source_branch>
        When the map_branch command is run
        Then an error should be raised

            Examples: Branches
                | source_branch     |
                | release-lts       |
                | release-4.2       |
                | release-5.0-lts   |
