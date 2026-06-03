from approvaltests import verify


def test_example_workflow_output_format() -> None:
    output = "input:  data/input.tif\noutput: data/output.tif\ncrs:    EPSG:4326\n"
    verify(output)
