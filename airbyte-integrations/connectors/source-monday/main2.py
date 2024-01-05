#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
import yaml
from airbyte_cdk.sources.declarative.yaml_declarative_source import YamlDeclarativeSource
from airbyte_cdk.sources.declarative.manifest_declarative_source import ManifestDeclarativeSource




if __name__ == "__main__":

    # file_path = '/Users/bytedance/dev/airbyte/airbyte-integrations/connectors/source-exchange-rates-test/source_yaml_base/connector-2/manifest.yaml'
    file_path = sys.argv[1]

# Open and read the YAML file
    with open(file_path, 'r') as file:
        try:
            data = file.read()  # Prints the content of the YAML file as a Python dictionary
        except yaml.YAMLError as exc:
            print(exc)

    # print (data)
    parsed_manifest = YamlDeclarativeSource._parse(data)
    source = ManifestDeclarativeSource(source_config=parsed_manifest, emit_connector_builder_messages=True)

    # source = SourceYamlBaseTest()
    # print (sys.argv)
    launch(source, sys.argv[2:])
