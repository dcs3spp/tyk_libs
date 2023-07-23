# pyright: reportUnusedImport=false

import pytest

from hamcrest import assert_that, equal_to
from unittest.mock import mock_open, patch

from docs.libs import links


def test_get_urls() -> None:
    expected = {
        "/basic-config-and-security/reduce-latency/caching/global-cache",
        "/graphql/introspection/introspection-queries",
        "/graphql/creating-gql-api",
        "/tyk-apis/tyk-dashboard-api/data-graphs-api",
        "/tyk-multi-data-centre/mdcb-components",
        "/tyk-on-premises/licensing",
        "/getting-started/key-concepts/graphql-entities",
        "/planning-for-production/database-settings/mongodb-sizing",
    }

    mocked_content = """
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

    mocked_content = mocked_content.strip(" \n")

    with patch.object(links.Path, "open", mock_open(read_data=mocked_content)):
        mock_path = links.Path("test_file.txt")

        result = {
            str(value.path) for value in links.get_path_set_from_urlcheck(mock_path)
        }

        assert_that(result, equal_to(expected))


def test_get_yaml_key() -> None:
    expected = {
        "/tyk-apis",
        "/debugging-series/debugging-series",
        "/debugging-series/mongodb-debugging",
        "/frequently-asked-questions",
        "/frequently-asked-questions/how-to-backup-tyk",
    }

    mocked_content = """
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

    with patch.object(links.Path, "open", mock_open(read_data=mocked_content)):
        mock_path = links.Path("test_file.txt")

        result = {
            str(value)
            for value in links.get_set_of_key_values_in_yaml(mock_path, "path")
        }

        assert_that(result, equal_to(expected))
