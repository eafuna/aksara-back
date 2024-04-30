from aksara.utils.general_chart_helpers import *
from aksara.utils.chart_builder import *
import os

from urllib.parse import urlparse
import boto3
from aksara.utils import triggers
import io

"""
Segregates chart types,
into respective chart builders
"""

def boto3_s3_get(input_file):


    s3Conn = boto3.resource(
        service_name='s3',
        region_name=os.environ["AWS_DEFAULT_REGION"],
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]        
    )

    input_parsed = urlparse(input_file)
    s3Obj = s3Conn.Object(input_parsed[1].split('.')[0], input_parsed[2].replace('/',''))
    buffer = io.BytesIO()
    s3Obj.download_fileobj(buffer)

    # import pdb;pdb.set_trace()
    triggers.send_telegram("......reading s3:"+input_file)

    return buffer

def build_chart(chart_type, data):
    variables = data["variables"]
    input_url = data["input"]

    input_file = boto3_s3_get(input_url)

    if chart_type == "bar_chart":
        return bar_chart(input_file, variables)
    elif chart_type == "heatmap_chart":
        return heatmap_chart(input_file, variables)
    elif chart_type == "timeseries_chart":
        return timeseries_chart(input_file, variables)
    elif chart_type == "bar_meter":
        return bar_meter(input_file, variables)
    elif chart_type == "custom_chart":
        return custom_chart(input_file, variables)
    elif chart_type == "snapshot_chart":
        return snapshot_chart(input_file, variables)
    elif chart_type == "waffle_chart":
        return waffle_chart(input_file, variables)
    elif chart_type == "helpers_custom":
        return helpers_custom(input_file)
    elif chart_type == "map_lat_lon":
        return map_lat_lon(input_file, variables)
    elif chart_type == "choropleth_chart":
        return choropleth_chart(input_file, variables)
    elif chart_type == "jitter_chart":
        return jitter_chart(input_file, variables)
    elif chart_type == "pyramid_chart":
        return pyramid_chart(input_file, variables)
    elif chart_type == "metrics_table":
        return metrics_table(input_file, variables)
    elif chart_type == "timeseries_shared":
        return timeseries_shared(input_file, variables)
    else:
        return {}
