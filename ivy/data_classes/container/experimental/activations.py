# global
from typing import Union, Optional, List, Dict

# local
import ivy
from ivy.data_classes.container.base import ContainerBase


class _ContainerWithActivationExperimental(ContainerBase):
    @staticmethod
    def static_logit(
        x: Union[float, int, ivy.Container],
        /,
        *,
        eps: Optional[float] = None,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.logit.
        This method simply wraps the function, and so the
        docstring for ivy.logit  also applies to this method with
        minimal changes.

        Parameters
        ----------
        x
            Input container.
        eps
            When eps is None the function outpus NaN where x < 0 or x > 1.
            and inf or -inf where x = 1 or x = 0, respectively.
            Otherwise if eps is defined, x is clamped to [eps, 1 - eps]
        out
            Optional output Contaner.

        Returns
        -------
        ret
            Container with logits of the leaves.

        Examples
        --------
        >>> a = ivy.array([1, 0, 0.9])
        >>> b = ivy.array([0.1, 2, -0.9])
        >>> x = ivy.Container(a=a, b=b)
        >>> z = ivy.Container.static_logit(x)
        >>> print(z)
        {
            a: ivy.array([inf, -inf, 2.19722438]),
            b: ivy.array([-2.19722462, nan, nan])
        }

        >>> a = ivy.array([0.3, 2, 0.9])
        >>> b = ivy.array([0.1, 1.2, -0.9])
        >>> x = ivy.Container(a=a, b=b)
        >>> z = ivy.Container.static_logit(x, eps=0.2)
        >>> print(z)
        {
            a: ivy.array([-0.84729779, 1.38629448, 1.38629448]),
            b: ivy.array([-1.38629436, 1.38629448, -1.38629436])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "logit",
            x,
            eps=eps,
            out=out,
        )

    def logit(
        self: Union[float, int, ivy.Container],
        /,
        *,
        eps: Optional[float] = None,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.logit.
        This method simply wraps the function, and so the
        docstring for ivy.logit  also applies to this method with
        minimal changes.

        Parameters
        ----------
        self
            Input container.
        eps
            When eps is None the function outpus NaN where x < 0 or x > 1.
            and inf or -inf where x = 1 or x = 0, respectively.
            Otherwise if eps is defined, x is clamped to [eps, 1 - eps]
        out
            Optional output Contaner.

        Returns
        -------
        ret
            Container with logits of the leaves.

        Examples
        --------
        >>> a = ivy.array([1, 0, 0.9])
        >>> b = ivy.array([0.1, 2, -0.9])
        >>> x = ivy.Container(a=a, b=b)
        >>> z = x.logit()
        >>> print(z)
        {
            a: ivy.array([inf, -inf, 2.19722438]),
            b: ivy.array([-2.19722462, nan, nan])
        }

        >>> a = ivy.array([0.3, 2, 0.9])
        >>> b = ivy.array([0.1, 1.2, -0.9])
        >>> x = ivy.Container(a=a, b=b)
        >>> z = x.logit(eps=0.2)
        >>> print(z)
        {
            a: ivy.array([-0.84729779, 1.38629448, 1.38629448]),
            b: ivy.array([-1.38629436, 1.38629448, -1.38629436])
        }

        """
        return self.static_logit(self, eps=eps, out=out)

    @staticmethod
    def static_thresholded_relu(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        threshold: Union[int, float] = 0,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.thresholded_relu.
        This method simply wraps the function, and so the docstring
        for ivy.thresholded_relu also applies to this method with minimal changes.

        Parameters
        ----------
        x
            input container.
        threshold
            threshold value above which the activation is linear. Default: ``0``.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output container, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            a container with the rectified linear activation unit function
            applied element-wise with custom threshold.

        Examples
        --------
        >>> x = ivy.Container(a=ivy.array([1.0, -1.2]), b=ivy.array([0.4, -0.2]))
        >>> y = ivy.Container.static_thresholded_relu(x, threshold=0.5)
        >>> print(y)
        {
            a: ivy.array([1., 0.]),
            b: ivy.array([0., 0.])
        }

        """
        return ContainerBase.cont_multi_map_in_function(
            "thresholded_relu",
            x,
            threshold=threshold,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def thresholded_relu(
        self: ivy.Container,
        /,
        *,
        threshold: Union[int, float] = 0,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.thresholded_relu.
        This method simply wraps the function, and so the docstring
        for ivy.thresholded_relu also applies to this method with minimal changes.

        Parameters
        ----------
        self
            input container.
        threshold
            threshold value above which the activation is linear. Default: ``0``.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output container, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            a container with the rectified linear activation unit function
            applied element-wise with custom threshold.

        Examples
        --------
        >>> x = ivy.Container(a=ivy.array([1.0, -1.2]), b=ivy.array([0.4, -0.2]))
        >>> y = x.thresholded_relu(threshold=0.5)
        >>> print(y)
        {
            a: ivy.array([1., 0.]),
            b: ivy.array([0., 0.])
        }

        """
        return self.static_thresholded_relu(
            self,
            threshold=threshold,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_prelu(
        x: Union[ivy.NativeArray, ivy.Array, ivy.Container],
        slope: Union[float, ivy.NativeArray, ivy.Array, ivy.Container],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """

        Parameters
        ----------
        x
        slope
        key_chains
        to_apply
        prune_unapplied
        map_sequences
        out
        """
        return ContainerBase.cont_multi_map_in_function(
            "prelu",
            x,
            slope,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def prelu(
        self: ivy.Container,
        slope: Union[float, ivy.NativeArray, ivy.Array, ivy.Container],
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """

        Parameters
        ----------
        slope
        key_chains
        to_apply
        prune_unapplied
        map_sequences
        out
        """
        return self.static_prelu(
            self,
            slope,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_relu6(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.relu6.
        This method simply wraps the function, and so the docstring
        for ivy.relu6 also applies to this method with minimal changes.

        Parameters
        ----------
        x
            input container.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output container, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            a container with the rectified linear 6 activation unit function
            applied element-wise.

        Examples
        --------
        >>> x = {
                    a: ivy.array([-3., -2., -1., 0., 1., 2., 3., 4., 5.]),
                    b: ivy.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])
                }
        >>> y = ivy.Container.static_relu6(x)
        >>> print(y)
        {
            a: ivy.array([0., 0., 0., 0., 1., 2., 3., 4., 5.]),
            b: ivy.array([1., 2., 3., 4., 5., 6., 6., 6., 6.])
        }

        """
        return ContainerBase.cont_multi_map_in_function(
            "relu6",
            x,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def relu6(
        self: ivy.Container,
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.relu6.
        This method simply wraps the function, and so the docstring
        for ivy.relu6 also applies to this method with minimal changes.

        Parameters
        ----------
        self
            input container.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.
        out
            optional output container, for writing the result to. It must have a shape
            that the inputs broadcast to.

        Returns
        -------
        ret
            a container with the rectified linear 6 activation unit function
            applied element-wise.

        Examples
        --------
        >>> x = {
                    a: ivy.array([-3., -2., -1., 0., 1., 2., 3., 4., 5.]),
                    b: ivy.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])
                }
        >>> y = x.relu()
        >>> print(y)
        {
            a: ivy.array([0., 0., 0., 0., 1., 2., 3., 4., 5.]),
            b: ivy.array([1., 2., 3., 4., 5., 6., 6., 6., 6.])
        }

        """
        return self.static_relu6(
            self,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    @staticmethod
    def static_batch_norm(
        x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        mean: Union[ivy.NativeArray, ivy.Array, ivy.Container],
        variance: Union[ivy.NativeArray, ivy.Array, ivy.Container],
        /,
        *,
        offset: Optional[Union[ivy.NativeArray, ivy.Array, ivy.Container]] = None,
        scale: Optional[Union[ivy.NativeArray, ivy.Array, ivy.Container]] = None,
        training: bool = False,
        eps: float = 1e-5,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.batch_norm.
        This method simply wraps the function, and so the docstring
        for ivy.batch_norm also applies to this method with minimal changes.

        Parameters
        ----------
        x
            Input container.
        mean
            A mean array for the input's normalization.
        variance
            A variance array for the input's normalization.
        offset
            An offset array. If present, will be added to the normalized input.
        scale
            A scale array. If present, the scale is applied to the normalized input.
        training
            If true, calculate and use the mean and variance of `x`. Otherwise, use the
            provided `mean` and `variance`.
        eps
            A small float number to avoid dividing by 0.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
             Container containing the normalized, scaled, offset values.
        """
        return ContainerBase.cont_multi_map_in_function(
            "batch_norm",
            x,
            mean,
            variance,
            scale=scale,
            offset=offset,
            training=training,
            eps=eps,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def batch_norm(
        self: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        mean: Union[ivy.NativeArray, ivy.Array, ivy.Container],
        variance: Union[ivy.NativeArray, ivy.Array, ivy.Container],
        /,
        *,
        offset: Optional[Union[ivy.NativeArray, ivy.Array, ivy.Container]] = None,
        scale: Optional[Union[ivy.NativeArray, ivy.Array, ivy.Container]] = None,
        training: bool = False,
        eps: float = 1e-5,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.batch_norm.
        This method simply wraps the function, and so the docstring
        for ivy.batch_norm also applies to this method with minimal changes.

        Parameters
        ----------
        self
            Input container.
        mean
            A mean array for the input's normalization.
        variance
            A variance array for the input's normalization.
        offset
            An offset array. If present, will be added to the normalized input.
        scale
            A scale array. If present, the scale is applied to the normalized input.
        training
            If true, calculate and use the mean and variance of `x`. Otherwise, use the
            provided `mean` and `variance`.
        eps
            A small float number to avoid dividing by 0.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
        ret
             Container containing the normalized, scaled, offset values.
        """
        return self.static_batch_norm(
            self,
            mean,
            variance,
            scale=scale,
            offset=offset,
            training=training,
            eps=eps,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    @staticmethod
    def static_logsigmoid(
        input: Union[ivy.Array, ivy.NativeArray, ivy.Container],
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.logsigmoid.
        This method simply wraps the function, and so the
        docstring for ivy.logsigmoid also applies to this method with
        minimal changes.

        Parameters
        ----------
        input
            Input container.
        key_chains
            The key-chains to apply or not apply the method to. Default is ``None``.
        to_apply
            If True, the method will be applied to key_chains, otherwise key_chains
            will be skipped. Default is ``True``.
        prune_unapplied
            Whether to prune key_chains for which the function was not applied.
            Default is ``False``.
        map_sequences
            Whether to also map method to sequences (lists, tuples).
            Default is ``False``.

        Returns
        -------
            Container with Log-sigmoid applied to the leaves.

        Examples
        --------
        >>> a = ivy.array([1, 0, 0.9])
        >>> b = ivy.array([0.1, 2, -0.9])
        >>> x = ivy.Container(a=a, b=b)
        >>> z = ivy.Container.static_logsigmoid(x)
        >>> print(z)
        {
            a: ivy.array([-0.31326169, -0.69314718, -0.34115386]),
            b: ivy.array([-0.64439666, -0.126928, -1.24115384])
        }

        >>> a = ivy.array([0.3, 2.5, 4.9])
        >>> b = ivy.array([0.1, 1.2, -9.])
        >>> x = ivy.Container(a=a, b=b)
        >>> z = ivy.Container.static_logsigmoid(x)
        >>> print(z)
        {
            a: ivy.array([-0.55435526, -0.07888974, -0.00741899]),
            b: ivy.array([-0.64439666, -0.26328245, -9.00012302])
        }
        """
        return ContainerBase.cont_multi_map_in_function(
            "logsigmoid",
            input,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )

    def logsigmoid(
        self: ivy.Container,
        /,
        *,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
    ) -> ivy.Container:
        """
        Applies element-wise Log-sigmoid of x i.e. log(1 / (1 + exp(-x)).

        Parameters
        ----------
        self
            Input container.

        Returns
        -------
            Container with Log-sigmoid applied to the leaves.
        """
        return self.static_logsigmoid(
            self,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
        )
