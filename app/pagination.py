def paginate(query_result, request, page_size=5):
    page = int(request.args.get("page", 1))
    start = (page - 1) * page_size
    end = start + page_size
    total = len(query_result)
    
    return {
        "results": [item.to_dict() for item in query_result[start:end]],
        "page": page,
        "total_pages": (total // page_size) + (1 if total % page_size > 0 else 0),
        "total_items": total,
    }
