from erpnext import frappe

def run_report(filters):
  project = filters.get("project")

  data = frappe.db.sql("""
    SELECT DATE(creation) as date, COUNT(*) as task_created_count
    FROM `tabTask`
    WHERE project = %s
    GROUP BY DATE(creation)
    ORDER BY date ASC
  """, (project,))

  return data

