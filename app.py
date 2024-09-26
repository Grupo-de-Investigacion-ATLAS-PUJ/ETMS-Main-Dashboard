# /app.py

import dash
from presentation.layout import create_layout  # Import from presentation layer
from business_logic.business_logic import register_callbacks  # Import from business logic layer

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app)

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

