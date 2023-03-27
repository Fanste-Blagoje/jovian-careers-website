from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:1234@localhost/jovian_careers?charset=utf8mb4")


def load_jobs_from_db():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))
        jobs = []
        for row in result.fetchall():
            jobs.append(dict(row))
        return jobs


def load_job_from_db(job_id):
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs where id = :val"), val=job_id)
        rows = result.fetchall()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])


def add_application_to_db(job_id, data):
    with engine.connect() as connection:
        query = text("insert into applications "
                     "(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) "
                     "values (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
        connection.execute(query,
                           job_id=job_id,
                           full_name=data['full_name'],
                           email=data['email'],
                           linkedin_url=data['linkedin_url'],
                           education=data['education'],
                           work_experience=data['work_experience'],
                           resume_url=data['resume_url'],
                           )
