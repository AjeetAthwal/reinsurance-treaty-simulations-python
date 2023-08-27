class XoLTreaty:
    def __init__(self, attachment, limit):
        self.attachment = attachment
        self.limit = limit

    def apply_treaty(self, loss):
        capped_loss = min(loss - self.attachment, self.limit)
        return max(capped_loss, 0)