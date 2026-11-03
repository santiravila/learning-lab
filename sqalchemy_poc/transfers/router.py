from fastapi import APIRouter

router = APIRouter(
    prefix="transfers",
    tags=["transfers"]
)

@router.post("")
def create_transfer(
    transfer_payload,
    service
):
    pass