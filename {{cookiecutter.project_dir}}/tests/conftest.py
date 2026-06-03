from __future__ import annotations

import numpy as np
import pytest
import xarray as xr


@pytest.fixture()
def sample_data_array() -> xr.DataArray:
    data = np.zeros((4, 4), dtype=np.float32)
    return xr.DataArray(
        data,
        dims=["y", "x"],
        attrs={"crs": "EPSG:4326"},
    )
