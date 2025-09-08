# Permissions and Groups Setup

## Groups
- **Editors**: Can create and edit books (`can_create`, `can_edit`)
- **Viewers**: Can view books (`can_view`)
- **Admins**: Can view, create, edit, and delete books (`can_view`, `can_create`, `can_edit`, `can_delete`)

## Permissions
- `can_view`: View books
- `can_create`: Create books
- `can_edit`: Edit books
- `can_delete`: Delete books

## Views
- `list_books`: Requires `can_view` permission
- `create_book`: Requires `can_create` permission
- `edit_book`: Requires `can_edit` permission
- `delete_book`: Requires `can_delete` permission
