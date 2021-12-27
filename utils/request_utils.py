from datetime import time

import requests


def get(url, headers=None, params=None):
    return requests.get(url=url, headers=headers, params=params).json()


def post(url, headers=None, json=None):
    return requests.post(url=url, headers=headers, json=json).json()


def delete(url, headers=None, params=None):
    return requests.delete(url=url, headers=headers, params=params).json()


def delete_page(url, headers, params):
    response = delete(url, headers, params)
    status_code = response["meta"]["code"]
    response_message = response["meta"]["code"]
    if status_code == 20000:
        print("delete successfully")
    else:
        print(
            "delete failed, status code: " + str(
                status_code) + ", error message: " + response_message + "\n request url: " + url)


def delete_all_pages(delete_get_url, unpublish_url_fmt, page_type, headers):
    url = delete_get_url + "?type=" + page_type
    response = get(url + "&limit=30", headers)
    status_code = response["meta"]["code"]
    response_message = response["meta"]["message"]
    if status_code == 20000:
        pages = response["data"]["pages"]
        pages.reverse()
        if len(pages) > 3:
            for page in pages[3:]:
                delete_url = delete_get_url + "/" + page["id"]
                if page["status"] == "published":
                    unpublish_url = unpublish_url_fmt.format(page_id=page["id"])
                    response = post(unpublish_url, headers, {})
                    if response["meta"]["code"] == 20000:
                        print("page unpublish successfully")
                        response = delete(delete_url, headers=headers)
                        if response["meta"]["code"] == 20000:
                            print("page delete successfully")
                        else:
                            print(
                                "delete page failed, status code: " + str(
                                    response["meta"]["code"]) + ", error message: " + response["meta"][
                                    "message"] + "\n request url: " + delete_url)
                    else:
                        print(
                            "unpublish page failed, status code: " + str(
                                response["meta"]["code"]) + ", error message: " + response["meta"][
                                "message"] + "\n request url: " + unpublish_url)
    else:
        print(
            "request failed, status code: " + str(
                status_code) + ", error message: " + response_message + "\n request url: " + url)
