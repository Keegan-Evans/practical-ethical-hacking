# Introduction to Active Directory

## Overview

#### What is Active Directory?

Like a phone book that stores objects like computers, users, or printers.
Used by Windows/in Windows domain networks. 

- Directory service developed by Microsoft to manage Windows domain
  networks.

- Stores information about various objects like computers, users, and
  printers. This lets these objects be accessed from throughout the
network.

- Authentication handled with *Kerberos* using *Kerberos tickets*. There
 
#### Why is Active Directory Important?

- It is the most important identity management service in the world.

- Can be exploited without ever attacking patchable exploits. Using
  features, trusts, components of Active Directory itself. External
networks are often very well fortified, but interally they are often very
weak.

## Physical Active Directory Components

#### Domain Controllers

- The most important component. It is a server with th AD DS server role
  installed that has been specifically promoted to a domain controller. It
provides many features for the AD domain.

- Host a copy of the AD Domain Services (DS) directory store, meaning it
  hosts the information about the other AD objects.

- Provides authentication and authorization services.

- In a "forest" it replicates updates to other domain controllers.

- Allow admin access for management of user accounts and network
  resources. You can add users, computers, policies, etc. 

- Not the only, but the top AD target. Don't forget about PII or
  proprietary information as well.

#### AD Data Store

- Ntds.dit: A very sensitive document that should be a target, it contains
  the all of the information stored in AD, including password hashes. 

- Default location `%SystemRoot%\NTDS` on all domain controllers. 

- Only accessible through the domain controller processes and protocols.

## Logical Active Directory Components

#### AD Schema

- Definitions of every object that can be created. It is the rulebook
  about object creations.

#### Domains

- Groups of objects managed in a organization.  In a small business, you
  may only need one. 
 
- An adminstrative boundary. Allows grouping of objects that have the same
  applied policies.

#### Trees

- A group of domains, or heirarch of domains in AD DS. 

- Share a contiguous namespace with the parent domain.

- Can have other child domains.

- By default, they have two-way transistive trust with other domains. 

#### Forest

- A collection of one or more domain trees.

- Share a common schema and configuration partition and global catalog to
  enable searching.

- Enable trusts between all domains.

- Rarely will you see forests.

#### Organizational Units (Ous)

- AD containers that can containers that hold users, groups, computers,
  etc.

#### Trusts

- Facilitate access between resources.

- Directional: From trustings domain to trusted domain.

- Transitive: Trust extended to all of the objects trusted by each of the
  party domains. 

#### Objects

What are inside of the OUs. 
