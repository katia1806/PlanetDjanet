db.createUser({
  user: 'user',
  pwd: 'userpwd',
  roles: [{ role: 'dbOwner', db: 'planet_djanet' }],
  mechanisms: ['SCRAM-SHA-1'],
})
