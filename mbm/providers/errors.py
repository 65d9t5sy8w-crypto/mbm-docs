class ProviderError(RuntimeError):
    pass


class ProviderUnavailableError(ProviderError):
    pass


class EvidenceIncompleteError(ProviderError):
    pass
