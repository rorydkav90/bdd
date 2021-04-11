Feature: Build docker file

    Scenario: Build a docker file
        Given the lift_app dockerfile
        And I am a developer
        When I build the lift_app docker image
        Then push the lift_app image to dockerhub with tag test