Feature: Find paths that are missing in menu yaml file
    In order to identity pages that are failing to load a sidebar menu in the new website
    As a DX team member
    I want a list of paths that exist in urlcheck.json but do not exist in menu.yaml 

    Background:
        Given a urlcheck file is mocked
        """
        {"path":"/basic-config-and-security/reduce-latency/caching/global-cache/","title":"Basic (Global) Caching", "file":"./content/basic-config-and-security/reduce-latency/caching/global-cache.md"}
        {"path":"/graphql/introspection/introspection-queries/","title":"Introspection queries", "file":"./content/graphql/introspection/introspection-queries.md"}
        {"path":"/graphql/creating-gql-api/", "title":"Create a GraphQL API", "file": "./content/graphql/creating-gql-api.md"}
        {"path":"/tyk-apis/tyk-dashboard-api/data-graphs-api/", "title":"Data Graphs API", "file": "./content/tyk-apis/tyk-dashboard-api/data-graphs-api.md"}
        {"path":"/tyk-multi-data-centre/mdcb-components/", "title":"MDCB Components", "file": "./content/tyk-multi-data-centre/mdcb-components.md"}
        {"path":"/tyk-on-premises/licensing/", "title":"Licensing and deployment models", "file": "./content/tyk-on-premises/licensing.md"}
        {"path":"/docs/getting-started/licencing", "file":"./content/tyk-on-premises/licensing.md", "alias":true}
        {"path":"/docs/getting-started/licensing", "file":"./content/tyk-on-premises/licensing.md", "alias":true}
        {"path":"/getting-started/key-concepts/graphql-entities/", "title":"GraphQL Entities", "file": "./content/getting-started/key-concepts/graphql-entities.md"}
        {"path":"/planning-for-production/database-settings/mongodb-sizing/", "title":"MongoDB Sizing", "file": "./content/planning-for-production/database-settings/mongodb-sizing.md"}
        """
        And a menu file is mocked
        """
        menu:
          - title: "Tyk APIs Reference"
            path: /tyk-apis
            category: Page
            show: True
          - title: "Debugging Series"
            category: Directory
            show: True
            menu:
            - title: "Debugging Series"
              path: /debugging-series/debugging-series
              category: Page
              show: True
            - title: "MongoDB Debugging"
              path: /debugging-series/mongodb-debugging
              category: Page
              show: True
          - title: "Frequently Asked Questions"
            category: Directory
            show: True
            menu:
            - title: "Frequently Asked Questions"
              path: /frequently-asked-questions
              category: Page
              show: True
            - title: "How to backup Tyk"
              path: /frequently-asked-questions/how-to-backup-tyk
              category: Page
              show: True
        """

    Scenario: File inputs are valid
        When the check_missing_links command is run
        Then the following missing links should be reported
        """
        {
            "expected": [
                {"path": "/getting-started/key-concepts/graphql-entities"},
                {"path": "/basic-config-and-security/reduce-latency/caching/global-cache"},
                {"path": "/tyk-apis/tyk-dashboard-api/data-graphs-api"},
                {"path": "/graphql/introspection/introspection-queries"},
                {"path": "/tyk-multi-data-centre/mdcb-components"},
                {"path": "/planning-for-production/database-settings/mongodb-sizing"},
                {"path": "/graphql/creating-gql-api"},
                {"path": "/tyk-on-premises/licensing"}
            ]
        }
        """
