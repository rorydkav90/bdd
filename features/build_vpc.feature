Feature: Build AWS VPC

    Scenario: Build AWS VPC
        Given the vpc module
        And I am an AWS developer
        When the config is correct
        Then build the vpc