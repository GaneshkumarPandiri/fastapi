def test_get_all_posts(authorized_client):
    resp = authorized_client.get("/posts/")
    print(resp.json(),"get all posts resp===")
    assert resp.status_code == 200