from API.main_api import MainApi

ma = MainApi()


def test_get_five():
    status, result = ma.get_last_five()
    print("\n")
    for item in result:
        print(item)
        print("\n")
    assert status == 200


# def test_delete_five_one():
#     status = ma.delete_last_one()
#     assert status == 204


# def test_delete_five():
#     status = ma.delete_last_five()
#     assert status == 204


# def test_get_categories():
#     status = ma.get_categories()
#     assert status == 200
#
#
# def test_post_category(): #bug1 (создает не уникальные категории) #bug2 (создает имена больше 14 символов)
#     status = ma.post_categories()
#     ma.get_categories()
#     assert status == 201


# def test_del_category():
#     ma.get_categories()
#     status = ma.del_categories()
#     assert status == 204
#     ma.get_categories()
#
#
# def test_archive_category():
#     status = ma.arhives_categories()
#     assert status == 200
#     ma.get_categories()

