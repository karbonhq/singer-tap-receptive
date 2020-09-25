
ENDPOINTS_CONFIG = {
    'accounts': {
        'path': '/accounts',
        'pk': ['id']
    },
    'features': {
        'path': '/features',
        'pk': ['id'],
        'params': {
            'order_dir': 'asc',
            'order_by': 'updated_at'
        }
    },
    'users': {
        'path': '/users',
        'pk': ['id'],
        'params': {
            'role': 'endUser'
        }
    },
    'votes': {
        'path': '/votes',
        'pk': ['id']
    }
}
