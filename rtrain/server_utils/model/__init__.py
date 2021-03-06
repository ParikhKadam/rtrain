#!/usr/bin/env python

import sqlalchemy as sa
import sqlalchemy.ext.declarative
import sqlalchemy.orm as orm

Base = sqlalchemy.ext.declarative.declarative_base()


class Job(Base):
    """Represent a job in the database."""
    __tablename__ = 'Jobs'

    id = sa.Column(sa.CHAR(32), primary_key=True)
    creation_time = sa.Column(sa.TIMESTAMP, default=sa.func.now())
    modification_time = sa.Column(sa.TIMESTAMP, default=sa.func.now())
    status = sa.Column(sa.REAL)
    finished = sa.Column(sa.INTEGER)
    job_type = sa.Column(sa.VARCHAR(16))
    training_jobs = orm.relationship(
        'TrainingJob',
        cascade='all,delete,delete-orphan',
        passive_deletes=True)
    training_results = orm.relationship(
        'TrainingResult',
        cascade='all,delete,delete-orphan',
        passive_deletes=True)


class TrainingJob(Base):
    """Represent a training job in the database."""
    __tablename__ = 'TrainingJobs'

    id = sa.Column(sa.INT, primary_key=True)

    job_id = sa.Column(
        sa.CHAR(32), sa.ForeignKey('Jobs.id', ondelete='CASCADE'))
    job = orm.relationship('Job', back_populates='training_jobs')

    training_job = sa.Column(sa.LargeBinary)
    job_checksum = sa.Column(sa.CHAR(64))


class TrainingResult(Base):
    """Represent the result of a job in the database."""
    __tablename__ = 'TrainingResults'

    id = sa.Column(sa.INT, primary_key=True)

    job_id = sa.Column(
        sa.CHAR(32), sa.ForeignKey('Jobs.id', ondelete='CASCADE'))
    job = orm.relationship('Job', back_populates='training_results')

    result_type = sa.Column(sa.VARCHAR(16))
    result = sa.Column(sa.LargeBinary)
