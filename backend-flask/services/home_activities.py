from datetime import datetime, timedelta, timezone
#To create spans, you need to get a Tracer
from opentelemetry import trace
from lib.db import db #query_wrap_object, query_wrap_array

#tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
    #logger.info("HomeActivities")
#Creating Spans
    #with tracer.start_as_current_span("home.activities-mock-data"):
        #span = trace.get_current_span()
        #now = datetime.now(timezone.utc).astimezone()
        #span.set_attribute("app.now", now.isoformat())
        
       # sql = query_wrap_array("""
       #SELECT * FROM activities          
       # """)
        #print (sql)
       # with pool.connection() as conn:
       #  with conn.cursor() as cur:
       #     cur.execute(sql)
       #      this will return a tuple
       #     the first field being the data
       #    json = cur.fetchone()
        #return json[0]
         #return results
      sql = db.template('activities','home')
      results = db.query_array_json(sql)
      return results
