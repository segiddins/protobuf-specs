# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: sigstore_trustroot.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto

from ...common import v1 as __common_v1__


@dataclass(eq=False, repr=False)
class TransparencyLogInstance(betterproto.Message):
    """
    TransparencyLogInstance describes the immutable parameters from a
    transparency log. See https://www.rfc-editor.org/rfc/rfc9162.html#name-log-
    parameters for more details. The included parameters are the minimal set
    required to identify a log, and verify an inclusion proof/promise.
    """

    base_url: str = betterproto.string_field(1)
    """The base URL at which can be used to URLs for the client."""

    hash_algorithm: "__common_v1__.HashAlgorithm" = betterproto.enum_field(2)
    """The hash algorithm used for the Merkle Tree."""

    public_key: "__common_v1__.PublicKey" = betterproto.message_field(3)
    """
    The public key used to verify signatures generated by the log. This
    attribute contains the signature algorithm used by the log.
    """

    log_id: "__common_v1__.LogId" = betterproto.message_field(4)
    """The unique identifier for this transparency log."""


@dataclass(eq=False, repr=False)
class CertificateAuthority(betterproto.Message):
    """
    CertificateAuthority enlists the information required to identify which CA
    to use and perform signature verification.
    """

    subject: "__common_v1__.DistinguishedName" = betterproto.message_field(1)
    """
    The root certificate MUST be self-signed, and so the subject and issuer are
    the same.
    """

    uri: str = betterproto.string_field(2)
    """
    The URI identifies the certificate authority. It is RECOMMENDED that the
    URI is the base URL for the certificate authority, that can be provided to
    any SDK/client provided by the certificate authority to interact with the
    certificate authority.
    """

    cert_chain: "__common_v1__.X509CertificateChain" = betterproto.message_field(3)
    """The certificate chain for this CA."""

    valid_for: "__common_v1__.TimeRange" = betterproto.message_field(4)
    """
    The time the *entire* chain was valid. This is at max the longest interval
    when *all* certificates in the chain were valid, but it MAY be shorter.
    Clients MUST check timestamps against *both* the `valid_for` time range
    *and* the entire certificate chain. The TimeRange should be considered
    valid *inclusive* of the endpoints.
    """


@dataclass(eq=False, repr=False)
class TrustedRoot(betterproto.Message):
    """
    TrustedRoot describes the client's complete set of trusted entities. How
    the TrustedRoot is populated is not specified, but can be a combination of
    many sources such as TUF repositories, files on disk etc. The TrustedRoot
    is not meant to be used for any artifact verification, only to capture the
    complete/global set of trusted verification materials. When verifying an
    artifact, based on the artifact and policies, a selection of
    keys/authorities are expected to be extracted and provided to the
    verification function. This way the set of keys/authorities can be kept to
    a minimal set by the policy to gain better control over what signatures
    that are allowed. The embedded transparency logs, CT logs, CAs and TSAs
    MUST include any previously used instance -- otherwise signatures made in
    the past cannot be verified. All the listed instances SHOULD be sorted by
    the 'valid_for' in ascending order, that is, the oldest instance first.
    Only the last instance is allowed to have their 'end' timestamp unset. All
    previous instances MUST have a closed interval of validity. The last
    instance MAY have a closed interval. Clients MUST accept instances that
    overlaps in time, if not clients may experience problems during rotations
    of verification materials. To be able to manage planned rotations of either
    transparency logs or certificate authorities, clienst MUST accept lists of
    instances where the last instance have a 'valid_for' that belongs to the
    future. This should not be a problem as clients SHOULD first seek the trust
    root for a suitable instance before creating a per artifact trust root
    (that is, a sub-set of the complete trust root) that is used for
    verification.
    """

    media_type: str = betterproto.string_field(1)
    """MUST be application/vnd.dev.sigstore.trustedroot+json;version=0.1"""

    tlogs: List["TransparencyLogInstance"] = betterproto.message_field(2)
    """A set of trusted Rekor servers."""

    certificate_authorities: List["CertificateAuthority"] = betterproto.message_field(3)
    """
    A set of trusted certificate authorities (e.g Fulcio), and any intermediate
    certificates they provide. If a CA is issuing multiple intermediate
    certificate, each combination shall be represented as separate chain. I.e,
    a single root cert may appear in multiple chains but with different
    intermediate and/or leaf certificates. The certificates are intended to be
    used for verifying artifact signatures.
    """

    ctlogs: List["TransparencyLogInstance"] = betterproto.message_field(4)
    """A set of trusted certificate transparency logs."""

    timestamp_authorities: List["CertificateAuthority"] = betterproto.message_field(5)
    """A set of trusted timestamping authorities."""
