"""first migration

Revision ID: 0bf685705413
Revises: 
Create Date: 2024-06-25 07:50:44.099941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bf685705413'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('annee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('departement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('salle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('filiere',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=200), nullable=False),
    sa.Column('departement_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['departement_id'], ['departement.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('utilisateur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('nom', sa.String(length=200), nullable=False),
    sa.Column('prenoms', sa.String(length=200), nullable=False),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('reset_token', sa.String(), nullable=True),
    sa.Column('token_expires', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id', 'role_id', name='unique_user_role'),
    sa.UniqueConstraint('username')
    )
    op.create_table('enseignant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matricule', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('specialite', sa.String(length=200), nullable=False),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.Column('departement_id', sa.Integer(), nullable=True),
    sa.Column('is_chef', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['departement_id'], ['departement.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['grade_id'], ['grade.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('matricule'),
    sa.UniqueConstraint('utilisateur_id')
    )
    op.create_table('etudiant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('matricule', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.Column('filiere_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['filiere_id'], ['filiere.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('matricule'),
    sa.UniqueConstraint('utilisateur_id')
    )
    op.create_table('utilisateur_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chef_departement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('enseignant_id', sa.Integer(), nullable=True),
    sa.Column('annee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['annee_id'], ['annee.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['enseignant_id'], ['enseignant.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jury',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.String(length=200), nullable=False),
    sa.Column('president_id', sa.Integer(), nullable=True),
    sa.Column('examinateur_id', sa.Integer(), nullable=True),
    sa.Column('rapporteur_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['examinateur_id'], ['enseignant.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['president_id'], ['enseignant.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['rapporteur_id'], ['enseignant.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('numero'),
    sa.UniqueConstraint('president_id', 'examinateur_id', 'rapporteur_id', name='uq_jury_composition'),
    schema='public'
    )
    op.create_table('soutenance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('theme', sa.String(length=200), nullable=True),
    sa.Column('lieu_stage', sa.String(length=200), nullable=True),
    sa.Column('responsable', sa.String(length=200), nullable=True),
    sa.Column('cahier_charge', sa.String(length=200), nullable=True),
    sa.Column('is_theme_valide', sa.Boolean(), nullable=True),
    sa.Column('is_binome_valide', sa.Boolean(), nullable=True),
    sa.Column('choix1_id', sa.Integer(), nullable=True),
    sa.Column('choix2_id', sa.Integer(), nullable=True),
    sa.Column('maitre_memoire_id', sa.Integer(), nullable=True),
    sa.Column('annee_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['annee_id'], ['annee.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['choix1_id'], ['enseignant.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['choix2_id'], ['enseignant.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['maitre_memoire_id'], ['enseignant.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['owner_id'], ['utilisateur.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('numero')
    )
    op.create_table('appartenir',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('etudiant_id', sa.Integer(), nullable=True),
    sa.Column('soutenance_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['etudiant_id'], ['etudiant.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['soutenance_id'], ['soutenance.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appartenir')
    op.drop_table('soutenance')
    op.drop_table('jury', schema='public')
    op.drop_table('chef_departement')
    op.drop_table('utilisateur_image')
    op.drop_table('etudiant')
    op.drop_table('enseignant')
    op.drop_table('utilisateur')
    op.drop_table('filiere')
    op.drop_table('salle')
    op.drop_table('role')
    op.drop_table('grade')
    op.drop_table('departement')
    op.drop_table('annee')
    # ### end Alembic commands ###
