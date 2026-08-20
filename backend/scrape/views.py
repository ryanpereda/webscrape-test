import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def api_home(request):
    return Response({
        "message": "Data Miner API is running"
    })

@api_view(["POST"])
def upload_csv(request):
    uploaded_file = request.FILES.get("file")

    if not uploaded_file:
        return Response(
            {"error": "No file was uploaded"},
            status=400
        )

    if not uploaded_file.name.endswith(".csv"):
        return Response(
            {"error": "Please upload a CSV file"},
            status=400
        )

    try:
        dataframe = pd.read_csv(uploaded_file)

        preview = dataframe.head().fillna("").to_dict(
            orient="records"
        )

        return Response({
            "filename": uploaded_file.name,
            "rows": len(dataframe),
            "columns": len(dataframe.columns),
            "column_names": dataframe.columns.tolist(),
            "preview": preview,
        })

    except Exception as error:
        return Response(
            {"error": str(error)},
            status=400
        )