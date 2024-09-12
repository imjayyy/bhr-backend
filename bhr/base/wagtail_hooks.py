from wagtail import hooks
from wagtail.admin import widgets
# from wagtail import menus

# @hooks.register('construct_main_menu')
# def hide_homepage_menu_item(request, menu):
#     # Hide the "Homepage" menu item
#     for item in menu.children:
#         if item.label == 'Homepage':  # Adjust if necessary
#             item.is_active = False

@hooks.register('construct_page_chooser_queryset')
def hide_homepage_in_chooser(request, pages):
    # Exclude the homepage from the page chooser
    return pages.exclude(id=1)
