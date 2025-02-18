import pytest
from playwright.sync_api import Page, expect, Route

def test_mock_api_fruits(page:Page):
    def handle_route_response(route:Route):
        json = [{"name":"Saaalima is mocking data",
                 "id": '22'}]
        route.fulfill(json=json)

    page.route("https://demo.playwright.dev/api-mocking/api/v1/fruits",handle_route_response)
    page.goto("https://demo.playwright.dev/api-mocking")

    expect(page.get_by_text("Saaalima is mocking data")).to_be_visible()
