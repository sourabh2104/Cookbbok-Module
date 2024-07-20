import frappe
from frappe.utils import flt

def execute(filters=None):
    columns, data = [], []
    
    # Define Columns
    columns = [
        {
            "fieldname": "date",
            "label": "Date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "fieldname": "task_created_count",
            "label": "Task Created Count",
            "fieldtype": "Int",
            "width": 150
        }
    ]

    # Fetch Data based on Filters
    if filters.get("project"):
        project = filters["project"]

        tasks = frappe.db.sql("""
            SELECT 
                DATE(date) AS date,
                COUNT(*) AS task_created_count
            FROM 
                tabTask
            WHERE
                project = %s
            GROUP BY 
                DATE(date)
            ORDER BY 
                DATE(date) ASC
        """, (project), as_dict=1)

        for task in tasks:
            data.append({
                "date": task.date,
                "task_created_count": task.task_created_count
            })

    return columns, data
