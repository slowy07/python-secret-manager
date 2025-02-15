#!/usr/bin/env python

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
"""
command line application and sample code for enabling a secret version.
"""

import argparse


# [START secretmanager_enable_secret_version_with_etag]
def enable_secret_version_with_etag(project_id, secret_id, version_id, etag):
    """
    Enable the given secret version, enabling it to be accessed after
    previously being disabled. Other secrets versions are unaffected.
    """

    # Import the Secret Manager client library.
    from google.cloud import secretmanager
    from google.cloud.secretmanager_v1.types import service

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Build the request
    request = service.EnableSecretVersionRequest()
    request.name = name
    request.etag = etag

    # Disable the secret version.
    response = client.enable_secret_version(request=request)

    print("Enabled secret version: {}".format(response.name))
    # [END secretmanager_enable_secret_version_with_etag]

    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("project_id", help="id of the GCP project")
    parser.add_argument("secret_id", help="id of the secret from which to act")
    parser.add_argument("version_id", help="id of the version to enable")
    parser.add_argument("etag", help="current etag of the version")
    args = parser.parse_args()

    enable_secret_version_with_etag(
        args.project_id, args.secret_id, args.version_id, args.etag)
